from flask import jsonify
from flask import Blueprint
from models import Model
from scalers.scalers import scaler1b

route1 = Blueprint('route1', __name__)

model = Model()


def pm10_index(val):
    if val <= 25.0:
        return 0
    elif 26.0 <= val <= 50.0:
        return 1
    elif 51.0 <= val <= 90.0:
        return 2
    elif 91.0 <= val <= 180.0:
        return 3
    else:
        return 4


@route1.route('/model1a')
def model1a():
    return jsonify(1)


@route1.route('/model1b')
def model1b():
    tmpDs = [[[8.00000000e+00, 1.00000000e+00, -2.61702128e+00,
               8.46153846e-01, -1.50000000e+00, 2.86666667e+00,
               -2.78070175e+00],
              [8.00000000e+00, 2.00000000e+00, -2.61702128e+00,
               8.46153846e-01, -1.58823529e+00, 2.85000000e+00,
               -2.85087719e+00],
              [8.00000000e+00, 3.00000000e+00, -2.61702128e+00,
               9.23076923e-01, -1.67647059e+00, 2.81666667e+00,
               -2.91228070e+00],
              [8.00000000e+00, 4.00000000e+00, -2.61702128e+00,
               1.00000000e+00, -1.76470588e+00, 2.80000000e+00,
               -2.87719298e+00],
              [8.00000000e+00, 5.00000000e+00, -2.61702128e+00,
               1.07692308e+00, -1.94117647e+00, 2.80000000e+00,
               -2.90350877e+00],
              [8.00000000e+00, 6.00000000e+00, -2.48936170e+00,
               1.15384615e+00, -2.02941176e+00, 2.78333333e+00,
               -2.89473684e+00],
              [8.00000000e+00, 7.00000000e+00, -2.36170213e+00,
               6.92307692e-01, -2.11764706e+00, 8.66666667e-01,
               -2.92982456e+00],
              [8.00000000e+00, 8.00000000e+00, -2.23404255e+00,
               1.53846154e-01, -2.11764706e+00, -1.06666667e+00,
               -2.94736842e+00],
              [8.00000000e+00, 9.00000000e+00, -2.10638298e+00,
               -3.07692308e-01, -2.11764706e+00, -2.98333333e+00,
               -2.89473684e+00],
              [8.00000000e+00, 1.00000000e+01, -1.97872340e+00,
               -5.38461538e-01, -2.20588235e+00, -1.10000000e+00,
               -2.90350877e+00],
              [8.00000000e+00, 1.10000000e+01, -1.85106383e+00,
               -8.46153846e-01, -2.29411765e+00, 7.83333333e-01,
               -2.92982456e+00],
              [8.00000000e+00, 1.20000000e+01, -1.72340426e+00,
               -1.07692308e+00, -2.38235294e+00, 2.65000000e+00,
               -2.92982456e+00],
              [8.00000000e+00, 1.30000000e+01, -1.72340426e+00,
               -8.46153846e-01, -2.47058824e+00, 9.83333333e-01,
               -2.84210526e+00],
              [8.00000000e+00, 1.40000000e+01, -1.85106383e+00,
               -6.92307692e-01, -2.64705882e+00, -7.00000000e-01,
               -2.85964912e+00],
              [8.00000000e+00, 1.50000000e+01, -1.97872340e+00,
               -4.61538462e-01, -2.82352941e+00, -2.36666667e+00,
               -2.89473684e+00],
              [8.00000000e+00, 1.60000000e+01, -1.97872340e+00,
               -3.84615385e-01, -2.82352941e+00, -1.65000000e+00,
               -2.86842105e+00],
              [8.00000000e+00, 1.70000000e+01, -2.10638298e+00,
               -2.30769231e-01, -2.82352941e+00, -9.33333333e-01,
               -2.96491228e+00],
              [8.00000000e+00, 1.80000000e+01, -2.23404255e+00,
               -7.69230769e-02, -2.82352941e+00, -2.16666667e-01,
               -2.69298246e+00],
              [8.00000000e+00, 1.90000000e+01, -2.23404255e+00,
               8.88178420e-16, -2.73529412e+00, -1.33333333e-01,
               -2.51754386e+00],
              [8.00000000e+00, 2.00000000e+01, -2.36170213e+00,
               7.69230769e-02, -2.55882353e+00, -5.00000000e-02,
               -2.69298246e+00],
              [8.00000000e+00, 2.10000000e+01, -2.36170213e+00,
               1.53846154e-01, -2.47058824e+00, 5.00000000e-02,
               -2.71052632e+00],
              [8.00000000e+00, 2.20000000e+01, -2.36170213e+00,
               5.38461538e-01, -2.47058824e+00, 1.00000000e-01,
               -2.66666667e+00],
              [8.00000000e+00, 2.30000000e+01, -2.36170213e+00,
               8.46153846e-01, -2.47058824e+00, 1.50000000e-01,
               -2.66666667e+00],
              [8.00000000e+00, 0.00000000e+00, -2.36170213e+00,
               1.23076923e+00, -2.38235294e+00, 2.16666667e-01,
               -2.72807018e+00],
              [8.00000000e+00, 1.00000000e+00, -2.23404255e+00,
               1.30769231e+00, -2.47058824e+00, 6.66666667e-02,
               -2.76315789e+00],
              [8.00000000e+00, 2.00000000e+00, -2.10638298e+00,
               1.38461538e+00, -2.55882353e+00, -1.00000000e-01,
               -2.77192982e+00],
              [8.00000000e+00, 3.00000000e+00, -2.10638298e+00,
               1.46153846e+00, -2.55882353e+00, -2.50000000e-01,
               -2.73684211e+00],
              [8.00000000e+00, 4.00000000e+00, -2.10638298e+00,
               1.69230769e+00, -2.64705882e+00, 8.00000000e-01,
               -2.78070175e+00],
              [8.00000000e+00, 5.00000000e+00, -2.10638298e+00,
               1.92307692e+00, -2.64705882e+00, 1.86666667e+00,
               -2.76315789e+00],
              [8.00000000e+00, 6.00000000e+00, -2.10638298e+00,
               2.07692308e+00, -2.64705882e+00, 2.91666667e+00,
               -2.71929825e+00],
              [8.00000000e+00, 7.00000000e+00, -1.97872340e+00,
               1.61538462e+00, -2.47058824e+00, 1.11666667e+00,
               -2.71929825e+00],
              [8.00000000e+00, 8.00000000e+00, -1.85106383e+00,
               1.15384615e+00, -2.38235294e+00, -6.83333333e-01,
               -2.66666667e+00],
              [8.00000000e+00, 9.00000000e+00, -1.72340426e+00,
               6.15384615e-01, -2.20588235e+00, -2.48333333e+00,
               -2.74561404e+00],
              [8.00000000e+00, 1.00000000e+01, -1.59574468e+00,
               4.61538462e-01, -2.38235294e+00, -2.48333333e+00,
               -2.70175439e+00],
              [8.00000000e+00, 1.10000000e+01, -1.59574468e+00,
               3.07692308e-01, -2.47058824e+00, -2.48333333e+00,
               -2.66666667e+00],
              [8.00000000e+00, 1.20000000e+01, -1.46808511e+00,
               1.53846154e-01, -2.64705882e+00, -2.48333333e+00,
               -2.65789474e+00],
              [8.00000000e+00, 1.30000000e+01, -1.59574468e+00,
               4.61538462e-01, -2.55882353e+00, -2.11666667e+00,
               -2.73684211e+00],
              [8.00000000e+00, 1.40000000e+01, -1.59574468e+00,
               7.69230769e-01, -2.55882353e+00, -1.76666667e+00,
               -2.78070175e+00],
              [8.00000000e+00, 1.50000000e+01, -1.72340426e+00,
               1.07692308e+00, -2.47058824e+00, -1.40000000e+00,
               -2.81578947e+00],
              [8.00000000e+00, 1.60000000e+01, -1.85106383e+00,
               1.38461538e+00, -2.38235294e+00, -1.33333333e+00,
               -2.87719298e+00],
              [8.00000000e+00, 1.70000000e+01, -1.85106383e+00,
               1.69230769e+00, -2.38235294e+00, -1.26666667e+00,
               -2.79824561e+00],
              [8.00000000e+00, 1.80000000e+01, -1.97872340e+00,
               2.07692308e+00, -2.29411765e+00, -1.20000000e+00,
               -2.64912281e+00],
              [8.00000000e+00, 1.90000000e+01, -1.97872340e+00,
               2.15384615e+00, -2.29411765e+00, -1.10000000e+00,
               -2.50877193e+00],
              [8.00000000e+00, 2.00000000e+01, -1.97872340e+00,
               2.23076923e+00, -2.38235294e+00, -1.01666667e+00,
               -2.51754386e+00],
              [8.00000000e+00, 2.10000000e+01, -1.97872340e+00,
               2.30769231e+00, -2.47058824e+00, -9.16666667e-01,
               -2.63157895e+00],
              [8.00000000e+00, 2.20000000e+01, -1.85106383e+00,
               2.30769231e+00, -2.47058824e+00, -8.33333333e-01,
               -2.64035088e+00],
              [8.00000000e+00, 2.30000000e+01, -1.72340426e+00,
               2.30769231e+00, -2.47058824e+00, -7.66666667e-01,
               -2.76315789e+00],
              [8.00000000e+00, 0.00000000e+00, -1.72340426e+00,
               2.23076923e+00, -2.47058824e+00, -7.00000000e-01,
               -2.73684211e+00],
              [8.00000000e+00, 1.00000000e+00, -1.72340426e+00,
               2.38461538e+00, -2.47058824e+00, -6.33333333e-01,
               -2.62280702e+00],
              [8.00000000e+00, 2.00000000e+00, -1.85106383e+00,
               2.53846154e+00, -2.55882353e+00, -5.66666667e-01,
               -2.68421053e+00],
              [8.00000000e+00, 3.00000000e+00, -1.97872340e+00,
               2.69230769e+00, -2.55882353e+00, -5.00000000e-01,
               -2.75438596e+00],
              [8.00000000e+00, 4.00000000e+00, -1.97872340e+00,
               2.61538462e+00, -2.55882353e+00, -2.00000000e-01,
               -2.74561404e+00],
              [8.00000000e+00, 5.00000000e+00, -1.85106383e+00,
               2.53846154e+00, -2.64705882e+00, 1.00000000e-01,
               -2.66666667e+00],
              [8.00000000e+00, 6.00000000e+00, -1.85106383e+00,
               2.53846154e+00, -2.64705882e+00, 4.00000000e-01,
               -2.71929825e+00],
              [8.00000000e+00, 7.00000000e+00, -1.72340426e+00,
               2.46153846e+00, -2.55882353e+00, 3.33333333e-01,
               -2.70175439e+00],
              [8.00000000e+00, 8.00000000e+00, -1.59574468e+00,
               2.46153846e+00, -2.55882353e+00, 2.66666667e-01,
               -2.67543860e+00],
              [8.00000000e+00, 9.00000000e+00, -1.46808511e+00,
               2.46153846e+00, -2.47058824e+00, 2.00000000e-01,
               -2.64912281e+00],
              [8.00000000e+00, 1.00000000e+01, -1.34042553e+00,
               2.30769231e+00, -2.11764706e+00, 1.66666667e-01,
               -2.64035088e+00],
              [8.00000000e+00, 1.10000000e+01, -1.34042553e+00,
               2.15384615e+00, -1.76470588e+00, 1.33333333e-01,
               -2.59649123e+00],
              [8.00000000e+00, 1.20000000e+01, -1.21276596e+00,
               2.00000000e+00, -1.41176471e+00, 1.00000000e-01,
               -2.53508772e+00],
              [8.00000000e+00, 1.30000000e+01, -1.21276596e+00,
               2.00000000e+00, -1.32352941e+00, 1.83333333e-01,
               -2.37719298e+00],
              [8.00000000e+00, 1.40000000e+01, -1.08510638e+00,
               2.00000000e+00, -1.23529412e+00, 2.83333333e-01,
               -2.57894737e+00],
              [8.00000000e+00, 1.50000000e+01, -1.08510638e+00,
               2.00000000e+00, -1.05882353e+00, 3.83333333e-01,
               -2.53508772e+00],
              [8.00000000e+00, 1.60000000e+01, -1.08510638e+00,
               1.92307692e+00, -1.23529412e+00, 4.00000000e-01,
               -2.23684211e+00],
              [8.00000000e+00, 1.70000000e+01, -1.08510638e+00,
               1.76923077e+00, -1.41176471e+00, 4.16666667e-01,
               -2.53508772e+00],
              [8.00000000e+00, 1.80000000e+01, -1.08510638e+00,
               1.69230769e+00, -1.58823529e+00, 4.50000000e-01,
               -2.78947368e+00],
              [8.00000000e+00, 1.90000000e+01, -1.21276596e+00,
               1.84615385e+00, -1.67647059e+00, 6.00000000e-01,
               -2.79824561e+00],
              [8.00000000e+00, 2.00000000e+01, -1.21276596e+00,
               1.92307692e+00, -1.76470588e+00, 7.50000000e-01,
               -2.50000000e+00],
              [8.00000000e+00, 2.10000000e+01, -1.34042553e+00,
               2.07692308e+00, -1.76470588e+00, 9.00000000e-01,
               -2.48245614e+00],
              [8.00000000e+00, 2.20000000e+01, -1.34042553e+00,
               2.00000000e+00, -1.94117647e+00, 8.16666667e-01,
               -2.23684211e+00],
              [8.00000000e+00, 2.30000000e+01, -1.34042553e+00,
               1.92307692e+00, -2.02941176e+00, 7.33333333e-01,
               -2.38596491e+00],
              [8.00000000e+00, 0.00000000e+00, -1.34042553e+00,
               1.92307692e+00, -2.11764706e+00, 6.50000000e-01,
               -2.63157895e+00]]]
    pred = model.get_model1b().predict(tmpDs)
    preds = scaler1b.inverse_transform(pred.reshape(-1, 1)).reshape(pred.shape)
    return_list = []
    for l in preds[0]:
        return_list.append(pm10_index(l[0]))
    return jsonify(return_list)


@route1.route('/model2a')
def model2a():
    return jsonify(2)


@route1.route('/model2b')
def model2b():
    return jsonify(2)


@route1.route('/model3a')
def model3a():
    return jsonify(3)


@route1.route('/model3b')
def model3b():
    return jsonify(3)
