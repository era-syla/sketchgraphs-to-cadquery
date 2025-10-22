import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.135, 0.13083).lineTo(0.065, 0.13083).lineTo(0.065, 0.08083).lineTo(0.135, 0.08083).lineTo(0.135, 0.13083).close()
solid=wp_sketch0.add(loop0).extrude(0.08313770589644051)
