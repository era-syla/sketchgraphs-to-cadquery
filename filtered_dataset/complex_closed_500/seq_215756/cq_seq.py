import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.14364, -0.01346).lineTo(-0.11824, -0.01346).lineTo(-0.11824, -0.00864).lineTo(-0.14364, -0.00864).lineTo(-0.14364, -0.01346).close()
solid=wp_sketch0.add(loop0).extrude(0.011549815789564193)
