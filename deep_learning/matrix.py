#!/usr/bin/env python
### 30181118
import tensorflow as tf
import time

m1 = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], name="mat1")
m2 = tf.Variable([[1, 2, 3], [4, 5, 6], [7, 8, 9]], name="mat2")

scalar = tf.constant(5)
number = tf.Variable(1, name="counter")

add_msg = tf.constant("\nResult of matrix addition\n")
mul_msg = tf.constant("\nResult of matrix multiplication\n")
scalar_mul_msg = tf.constant("\nResults of scalar multiplication\n")
number_mul_msg = tf.constant("\nResults of number multiplication\n")

mat_add = tf.add(m1, m2)
mat_mul = tf.matmul(m1, m2)
mat_scalar_mul = tf.multiply(scalar, mat_mul)
mat_number_mul = tf.multiply(number, mat_mul)

init_op = tf.initialize_all_variables()
sess = tf.Session()
tf.device("/cpu:0")
sess.run(init_op)

for i in range(1, 100):
    print("\nFor i ={0}".format(i))
    print(sess.run(add_msg))
    print(sess.run(mat_add))

    print(sess.run(mul_msg))
    print(sess.run(mat_mul))

    print(sess.run(scalar_mul_msg))
    print(sess.run(mat_scalar_mul))

    update = tf.assign(number, tf.constant(i))  # update number
    sess.run(update)

    print(sess.run(number_mul_msg))
    print(sess.run(mat_number_mul))

    time.sleep(0.1)

sess.close()
