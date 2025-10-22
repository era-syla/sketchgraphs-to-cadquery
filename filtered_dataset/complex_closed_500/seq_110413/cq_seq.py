import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.3683, -0.48895).lineTo(0.3683, -0.48895).lineTo(0.3683, 0.28575).lineTo(-0.3683, 0.28575).lineTo(-0.3683, -0.48895).close()
solid=wp_sketch0.add(loop0).extrude(-1.1838327216673061)
