import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.09907, -0.12298).lineTo(-0.05455, -0.00382).lineTo(-0.0579, -0.00382).lineTo(-0.10263, -0.12341).lineTo(-0.11848, -0.12191).lineTo(-0.11987, -0.12517).lineTo(-0.11155, -0.12637).lineTo(-0.10905, -0.12599).lineTo(-0.0995, -0.12689).lineTo(-0.09907, -0.12298).close()
solid=wp_sketch0.add(loop0).extrude(-0.08535101620595877)
