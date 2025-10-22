import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.36634, -0.0254).lineTo(-0.32025, -0.0254).lineTo(-0.14618, -0.26515).lineTo(-0.14618, -0.3048).lineTo(-0.21485, -0.3048).lineTo(-0.36634, -0.0254).close()
solid=wp_sketch0.add(loop0).extrude(0.0319331414073276)
