import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.01502).threePointArc((-0.01502, -0.0), (0.0, -0.01502)).lineTo(-0.0, 0.01502).close()
solid=wp_sketch0.add(loop0).extrude(0.0574162687383602)
