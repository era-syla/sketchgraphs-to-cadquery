import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00175, 0.00425).lineTo(0.00675, 0.00425).lineTo(0.00675, 0.00275).lineTo(0.00175, 0.00275).lineTo(0.00175, 0.00425).close()
solid=wp_sketch0.add(loop0).extrude(0.008479142189105638)
