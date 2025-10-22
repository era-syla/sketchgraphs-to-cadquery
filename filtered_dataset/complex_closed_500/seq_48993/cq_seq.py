import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04416, -0.00498).lineTo(-0.04204, -0.00498).lineTo(-0.04204, 0.00498).lineTo(-0.04416, 0.00498).lineTo(-0.04416, -0.00498).close()
solid=wp_sketch0.add(loop0).extrude(0.029307977624355802)
