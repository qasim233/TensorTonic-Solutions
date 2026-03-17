import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.asarray(param)
    grad = np.asarray(grad)
    m = np.asarray(m)
    v = np.asarray(v)
    
    m_new = m * beta1+ grad * (1 - beta1) 
    v_new = v * beta2 + grad**2 * (1 - beta2)

    m_hat = m_new / (1 - beta1**t) 
    v_hat = v_new / (1 - beta2**t)

    param_new = param - lr * (m_hat / (np.sqrt(v_hat) + eps))
    return param_new, m_new, v_new