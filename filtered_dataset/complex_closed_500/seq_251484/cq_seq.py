import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1143, 0.0254).threePointArc((-0.1397, 0.0), (-0.1143, -0.0254)).lineTo(0.1143, -0.0254).threePointArc((0.1397, 0.0), (0.1143, 0.0254)).lineTo(-0.1143, 0.0254).close()
solid=wp_sketch0.add(loop0).extrude(-0.143648600002518)
