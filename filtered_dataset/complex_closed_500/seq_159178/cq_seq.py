import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00305, 0.00305).lineTo(-1.52705, 0.00305).lineTo(-1.52705, 1.98425).lineTo(-0.00305, 1.98425).lineTo(-0.00305, 0.00305).close()
solid=wp_sketch0.add(loop0).extrude(1.2522018543387892)
