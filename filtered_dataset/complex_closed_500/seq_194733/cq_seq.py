import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00159, -0.0254).lineTo(-0.00159, -0.0254).lineTo(-0.00159, 0.0254).lineTo(0.00159, 0.0254).lineTo(0.04921, 0.0254).lineTo(0.04921, 0.02223).lineTo(0.00159, 0.02223).lineTo(0.00159, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(-0.037424281105764956)
