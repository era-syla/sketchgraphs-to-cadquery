import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00217, 0.0).lineTo(0.04897, 0.0).lineTo(0.04897, 0.0468).lineTo(0.00217, 0.0468).lineTo(0.00217, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.13658468184377032)
