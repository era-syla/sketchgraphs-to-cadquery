import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03842, 0.0076).lineTo(0.06318, 0.0076).lineTo(0.06318, 0.07463).lineTo(0.03636, 0.07463).lineTo(0.03636, 0.03395).lineTo(-0.01467, 0.03395).lineTo(-0.01467, 0.0744).lineTo(-0.04101, 0.0744).lineTo(-0.03842, 0.0076).close()
solid=wp_sketch0.add(loop0).extrude(0.05691998827216592)
