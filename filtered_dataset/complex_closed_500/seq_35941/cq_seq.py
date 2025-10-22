import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.031, 0.001).lineTo(-0.039, 0.001).lineTo(-0.039, 0.0045).lineTo(-0.031, 0.0045).lineTo(-0.031, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(-0.0029220753680971505)
