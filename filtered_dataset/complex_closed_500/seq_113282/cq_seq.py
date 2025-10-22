import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0127, 0.1016).lineTo(-0.0127, 0.0889).lineTo(-0.0, 0.0889).lineTo(0.0127, 0.0889).lineTo(0.0127, 0.1016).lineTo(0.0127, 0.1143).lineTo(0.0, 0.1143).lineTo(-0.0127, 0.1143).lineTo(-0.0127, 0.1016).close()
solid=wp_sketch0.add(loop0).extrude(-0.04616532515301855)
