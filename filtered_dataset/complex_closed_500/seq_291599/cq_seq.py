import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.04).lineTo(0.03, 0.04).lineTo(0.03, 0.02).lineTo(0.06, 0.02).lineTo(0.06, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.11485708535746617)
