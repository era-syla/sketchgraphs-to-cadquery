import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06112, 0.02075).lineTo(0.05859, 0.02692).lineTo(0.05867, 0.02718).lineTo(0.05074, 0.02945).lineTo(0.05066, 0.0292).lineTo(0.04525, 0.0253).lineTo(0.06112, 0.02075).close()
solid=wp_sketch0.add(loop0).extrude(0.02474503684846314)
