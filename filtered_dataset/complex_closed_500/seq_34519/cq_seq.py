import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.16927, -0.02858).threePointArc((0.17245, -0.0254), (0.16927, -0.02223)).lineTo(0.16607, -0.02223).lineTo(0.16607, -0.01905).lineTo(0.16927, -0.01905).threePointArc((0.17562, -0.0254), (0.16927, -0.03175)).lineTo(0.16607, -0.03175).lineTo(0.16607, -0.02858).lineTo(0.16927, -0.02858).close()
solid=wp_sketch0.add(loop0).extrude(-0.010683058106637028)
