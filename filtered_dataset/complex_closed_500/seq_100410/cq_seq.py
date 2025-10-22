import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.26035, -0.02778).lineTo(-0.13335, -0.02778).lineTo(-0.13335, -0.0254).lineTo(-0.26035, -0.0254).lineTo(-0.26035, -0.02778).close()
solid=wp_sketch0.add(loop0).extrude(-0.3648874176545668)
