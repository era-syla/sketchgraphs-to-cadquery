import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05022, 0.20885).lineTo(-0.05022, 0.20885).lineTo(-0.05022, 0.23475).lineTo(0.05022, 0.23475).lineTo(0.05022, 0.20885).close()
solid=wp_sketch0.add(loop0).extrude(0.2733034129471305)
