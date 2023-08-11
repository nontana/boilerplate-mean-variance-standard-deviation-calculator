import numpy as np

def calculate(list):
  if len(list)==9:
    ToArr = np.array(list)
    ToArr = ToArr.reshape(3,3)
  ##
    calculations = {'mean': [ToArr.mean(axis=0).tolist(), ToArr.mean(axis=1).tolist(),ToArr.mean()],
                    'variance': [ToArr.var(axis=0).tolist(), ToArr.var(axis=1).tolist(),ToArr.var()],
                    'standard deviation': [ToArr.std(axis=0).tolist(), ToArr.std(axis=1).tolist(),ToArr.std()],
                    'max': [ToArr.max(axis=0).tolist(), ToArr.max(axis=1).tolist(),ToArr.max()],
                    'min': [ToArr.min(axis=0).tolist(), ToArr.min(axis=1).tolist(),ToArr.min()],
                    'sum': [ToArr.sum(axis=0).tolist(), ToArr.sum(axis=1).tolist(),ToArr.sum()]
    }
  else:
    raise ValueError("List must contain nine numbers.")
  return calculations
