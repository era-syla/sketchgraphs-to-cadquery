import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.045, 0.035).lineTo(-0.0125, 0.035).lineTo(-0.0125, 0.01).lineTo(0.0125, 0.01).lineTo(0.0125, 0.035).lineTo(0.045, 0.035).lineTo(0.045, 0.0).lineTo(-0.045, 0.0).lineTo(-0.045, 0.035).close()
solid=wp_sketch0.add(loop0).extrude(0.2598685729167212)
