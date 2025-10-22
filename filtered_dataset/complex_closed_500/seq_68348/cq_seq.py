import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0381, -0.68319).lineTo(0.0, -0.68319).lineTo(0.0, -0.64509).lineTo(0.0381, -0.64509).lineTo(0.0381, -0.68319).close()
solid=wp_sketch0.add(loop0).extrude(0.11326951784220579)
