import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.64406, 0.54751).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.2654881472465085)
