import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.5334, 0.0).lineTo(0.5334, 0.40005).lineTo(0.52388, 0.40005).lineTo(0.508, 0.635).lineTo(0.0, 0.635).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(1.6962729674914079)
