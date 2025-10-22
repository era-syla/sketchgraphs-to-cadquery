import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.2921, -0.0254).lineTo(0.2921, -0.0254).lineTo(0.2921, 0.0254).lineTo(-0.2921, 0.0254).lineTo(-0.2921, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(-0.14939871983915645)
