import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.1623, 0.34423).lineTo(0.2377, 0.34423).lineTo(0.2377, 0.29423).lineTo(-0.1623, 0.29423).lineTo(-0.1623, 0.34423).close()
solid=wp_sketch0.add(loop0).extrude(-0.7749251621354007)
