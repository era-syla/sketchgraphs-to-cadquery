import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0053).lineTo(0.00281, 0.0).lineTo(0.00281, -0.00802).lineTo(0.01921, -0.00802).lineTo(0.02282, -0.0).lineTo(0.02282, 0.0053).lineTo(0.0, 0.0053).close()
solid=wp_sketch0.add(loop0).extrude(-0.013883820363634107)
