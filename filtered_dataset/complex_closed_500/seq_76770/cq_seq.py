import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00863, -0.0205).lineTo(-0.00887, -0.0205).lineTo(-0.00887, -0.002).lineTo(0.00863, -0.002).lineTo(0.00863, -0.0205).close()
solid=wp_sketch0.add(loop0).extrude(0.020980288745918497)
