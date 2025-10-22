import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01905, 0.0).lineTo(-0.01905, -0.01588).lineTo(0.03175, -0.0254).lineTo(0.03175, 0.0).lineTo(-0.01905, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.039323898305857856)
