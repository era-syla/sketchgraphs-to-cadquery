import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00774, 0.001).lineTo(0.00725, 0.001).lineTo(0.00725, -0.001).lineTo(-0.00774, -0.001).lineTo(-0.00774, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(-0.017570929268100517)
