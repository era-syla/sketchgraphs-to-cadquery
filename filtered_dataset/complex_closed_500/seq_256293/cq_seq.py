import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(5.5372, 0.0).lineTo(11.6332, 0.0).lineTo(11.6332, 2.5908).lineTo(5.5372, 2.5908).lineTo(5.5372, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(14.308489451933005)
