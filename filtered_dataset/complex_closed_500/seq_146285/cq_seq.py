import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.2905, 0.9525).lineTo(-0.3035, 0.9525).lineTo(-0.3035, 0.8097).lineTo(-0.2905, 0.8097).lineTo(-0.2905, 0.9525).close()
solid=wp_sketch0.add(loop0).extrude(0.18046294163630242)
