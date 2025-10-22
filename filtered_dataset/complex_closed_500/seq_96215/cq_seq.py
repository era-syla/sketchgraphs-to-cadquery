import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.6096, 23.9522).lineTo(-0.6096, -0.6096).lineTo(13.2334, -0.6096).lineTo(13.2334, 6.7056).lineTo(8.6614, 6.7056).lineTo(8.6614, 9.9314).lineTo(10.9728, 9.9314).lineTo(10.9728, 19.685).lineTo(6.096, 19.685).lineTo(6.096, 23.9522).lineTo(-0.6096, 23.9522).close()
solid=wp_sketch0.add(loop0).extrude(55.01841053146032)
