import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.475, 0.0).lineTo(-0.39, 0.0).lineTo(-0.39, -0.021).lineTo(-0.475, -0.021).lineTo(-0.475, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.007907197397436136)
