import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.04715).lineTo(0.0762, 0.04715).lineTo(0.0762, 0.0138).lineTo(0.0762, 0.00763).lineTo(0.0, 0.00763).lineTo(0.0, 0.01886).lineTo(0.0, 0.04715).close()
solid=wp_sketch0.add(loop0).extrude(-0.057435110287944964)
