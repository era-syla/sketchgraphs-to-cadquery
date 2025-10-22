import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01056, -0.004).lineTo(0.00756, -0.004).lineTo(0.00756, -0.024).lineTo(0.01056, -0.024).lineTo(0.01056, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(-0.001654566708190881)
