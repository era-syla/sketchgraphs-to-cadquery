import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.008, 0.00423).lineTo(-0.012, 0.00423).lineTo(-0.012, 0.01663).lineTo(-0.008, 0.01663).lineTo(-0.008, 0.00423).close()
solid=wp_sketch0.add(loop0).extrude(-0.028400977408587078)
