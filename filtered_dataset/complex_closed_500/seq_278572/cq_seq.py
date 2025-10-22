import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.072, 0.03775).lineTo(0.1205, 0.03775).lineTo(0.1205, -0.03775).lineTo(0.072, -0.03775).lineTo(0.072, 0.03775).close()
solid=wp_sketch0.add(loop0).extrude(0.10818347123848039)
