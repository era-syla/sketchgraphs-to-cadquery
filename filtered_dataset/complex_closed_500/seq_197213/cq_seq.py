import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01693, 0.0386).lineTo(0.01693, 0.0386).lineTo(0.01693, -0.0436).lineTo(-0.01693, -0.0436).lineTo(-0.01693, 0.0386).close()
solid=wp_sketch0.add(loop0).extrude(0.22080407591508316)
