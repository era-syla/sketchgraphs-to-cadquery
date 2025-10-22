import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-23.29134, -0.002).lineTo(-23.84592, -0.002).lineTo(-23.84592, 0.324).lineTo(-23.29134, 0.324).lineTo(-23.29134, -0.002).close()
solid=wp_sketch0.add(loop0).extrude(-1.0910523353723136)
