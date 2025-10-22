import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1016, 0.0127).lineTo(0.0254, 0.0127).lineTo(0.0254, -0.0127).lineTo(0.1016, -0.0127).lineTo(0.1016, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.11134418936758149)
