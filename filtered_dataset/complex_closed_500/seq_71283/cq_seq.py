import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0127, -0.0254).lineTo(-0.0127, -0.0254).lineTo(-0.0127, 0.0254).lineTo(0.0127, 0.0254).lineTo(0.0127, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(0.1288231807884666)
