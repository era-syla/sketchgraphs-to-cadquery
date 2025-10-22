import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1016, 0.31158).lineTo(-0.0889, 0.31158).lineTo(0.04889, 0.10974).lineTo(0.0781, 0.10974).lineTo(0.1016, 0.31158).close()
solid=wp_sketch0.add(loop0).extrude(0.06464528745078235)
