import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04445, 0.06317).lineTo(-0.04445, 0.06317).lineTo(-0.04445, 0.10127).lineTo(0.04445, 0.10127).lineTo(0.04445, 0.06317).close()
solid=wp_sketch0.add(loop0).extrude(0.1683054939910472)
