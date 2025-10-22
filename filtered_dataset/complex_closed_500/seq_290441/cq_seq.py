import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04445, -0.0254).lineTo(0.04445, -0.0254).lineTo(0.04445, -0.02857).lineTo(-0.04445, -0.02857).lineTo(-0.04445, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(-0.19420150987673984)
