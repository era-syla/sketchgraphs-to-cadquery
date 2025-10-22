import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0558, -0.1075).lineTo(-0.0558, 0.1075).lineTo(-0.0555, 0.1075).lineTo(-0.0555, 0.1058).lineTo(0.0, 0.1058).lineTo(0.0, 0.1055).lineTo(-0.0555, 0.1055).lineTo(-0.0555, -0.1075).lineTo(-0.0558, -0.1075).close()
solid=wp_sketch0.add(loop0).extrude(-0.41204472795626707)
