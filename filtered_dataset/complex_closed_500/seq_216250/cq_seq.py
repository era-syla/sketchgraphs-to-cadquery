import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.007, -0.003).lineTo(-0.007, -0.00499).lineTo(-0.00872, -0.004).lineTo(-0.007, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.002504571032745505)
