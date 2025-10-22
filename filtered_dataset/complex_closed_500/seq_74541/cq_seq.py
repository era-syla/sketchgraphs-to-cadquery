import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.12037, 0.0244).lineTo(-0.07549, 0.0244).lineTo(-0.07549, -0.03844).lineTo(-0.12037, -0.03844).lineTo(-0.12037, 0.0244).close()
solid=wp_sketch0.add(loop0).extrude(0.14372138667818113)
