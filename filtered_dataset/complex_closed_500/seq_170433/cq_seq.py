import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0381, 0.4699).lineTo(-5.5245, 0.4699).lineTo(-5.5245, 0.18415).lineTo(-0.0381, 0.18415).lineTo(-0.0381, 0.4699).close()
solid=wp_sketch0.add(loop0).extrude(13.82532008758012)
