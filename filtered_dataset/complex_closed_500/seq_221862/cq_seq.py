import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02511, 0.11729).lineTo(0.02489, 0.11729).lineTo(0.02489, 0.11229).lineTo(-0.02511, 0.11229).lineTo(-0.02511, 0.11729).close()
solid=wp_sketch0.add(loop0).extrude(0.0547352478429656)
